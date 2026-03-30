# Rafael Waltrick
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from infra.database import get_db
from infra.orm.ProdutoModel import ProdutoDB
from infra.dependencies import get_current_active_user, require_group
from domain.schemas.AuthSchema import FuncionarioAuth
from domain.schemas.ProdutoSchema import ProdutoCreate, ProdutoUpdate, ProdutoResponse

router = APIRouter()

@router.get(
    "/produto/cardapio",
    tags=["Produto"],
    status_code=status.HTTP_200_OK,
    summary="Listar produtos para cardápio - pública"
)
async def get_produtos_publico(db: Session = Depends(get_db)):
    try:
        produtos = db.query(ProdutoDB).all()
        return [
            {
                "nome": produto.nome,
                "descricao": produto.descricao,
                "foto": produto.foto
            }
            for produto in produtos
        ]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar produtos do cardápio: {str(e)}"
        )

@router.get(
    "/produto/",
    response_model=list[ProdutoResponse],
    tags=["Produto"],
    status_code=status.HTTP_200_OK,
    summary="Listar todos os produtos - protegida"
)
async def get_produtos(
    db: Session = Depends(get_db),
    current_user: FuncionarioAuth = Depends(get_current_active_user)
):
    try:
        produtos = db.query(ProdutoDB).all()
        return produtos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar produtos: {str(e)}"
        )

@router.get(
    "/produto/{id}",
    response_model=ProdutoResponse,
    tags=["Produto"],
    status_code=status.HTTP_200_OK,
    summary="Buscar produto por ID - protegida"
)
async def get_produto(
    id: int,
    db: Session = Depends(get_db),
    current_user: FuncionarioAuth = Depends(get_current_active_user)
):
    try:
        produto = db.query(ProdutoDB).filter(ProdutoDB.id == id).first()
        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado"
            )
        return produto
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar produto: {str(e)}"
        )

@router.post(
    "/produto/",
    response_model=ProdutoResponse,
    tags=["Produto"],
    status_code=status.HTTP_201_CREATED,
    summary="Criar produto - grupo 1"
)
async def post_produto(
    produto_data: ProdutoCreate,
    db: Session = Depends(get_db),
    current_user: FuncionarioAuth = Depends(require_group([1]))
):
    try:
        novo_produto = ProdutoDB(
            id=None,
            nome=produto_data.nome,
            descricao=produto_data.descricao,
            foto=produto_data.foto,
            valor_unitario=produto_data.valor_unitario
        )

        db.add(novo_produto)
        db.commit()
        db.refresh(novo_produto)
        return novo_produto

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar produto: {str(e)}"
        )

@router.put(
    "/produto/{id}",
    response_model=ProdutoResponse,
    tags=["Produto"],
    status_code=status.HTTP_200_OK,
    summary="Atualizar produto - grupo 1"
)
async def put_produto(
    id: int,
    produto_data: ProdutoUpdate,
    db: Session = Depends(get_db),
    current_user: FuncionarioAuth = Depends(require_group([1]))
):
    try:
        produto = db.query(ProdutoDB).filter(ProdutoDB.id == id).first()
        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado"
            )

        update_data = produto_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(produto, field, value)

        db.commit()
        db.refresh(produto)
        return produto

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar produto: {str(e)}"
        )

@router.delete(
    "/produto/{id}",
    tags=["Produto"],
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Excluir produto - grupo 1"
)
async def delete_produto(
    id: int,
    db: Session = Depends(get_db),
    current_user: FuncionarioAuth = Depends(require_group([1]))
):
    try:
        produto = db.query(ProdutoDB).filter(ProdutoDB.id == id).first()
        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado"
            )

        db.delete(produto)
        db.commit()
        return None

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao deletar produto: {str(e)}"
        )