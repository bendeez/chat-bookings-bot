"""implemented general account logic into one table

Revision ID: a9c2501abc7a
Revises: cc0d25455300
Create Date: 2024-08-11 12:29:38.276257

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "a9c2501abc7a"
down_revision: Union[str, None] = "cc0d25455300"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("business", "account_type_id")
    op.add_column(
        "users", sa.Column("account_type", sa.String(length=45), nullable=False)
    )
    op.drop_constraint("users_ibfk_4", "users", type_="foreignkey")
    op.create_foreign_key(None, "users", "accounts", ["account_type"], ["account_type"])
    op.drop_column("users", "account_type_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "account_type_id", mysql.INTEGER(), autoincrement=False, nullable=False
        ),
    )
    op.drop_constraint(None, "users", type_="foreignkey")
    op.create_foreign_key(
        "users_ibfk_4", "users", "account_types", ["account_type_id"], ["id"]
    )
    op.drop_column("users", "account_type")
    op.add_column(
        "business",
        sa.Column(
            "account_type_id", mysql.INTEGER(), autoincrement=False, nullable=False
        ),
    )
    op.create_index("idx_account_type", "accounts", ["account_type"], unique=False)
    # ### end Alembic commands ###
