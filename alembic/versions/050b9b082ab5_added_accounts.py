"""added accounts

Revision ID: 050b9b082ab5
Revises: 413f5e06d20f
Create Date: 2024-08-11 11:26:08.756000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "050b9b082ab5"
down_revision: Union[str, None] = "413f5e06d20f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "accounts",
        sa.Column("account_type", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["account_type"],
            ["account_types.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("business", sa.Column("account_type", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "business", "account_types", ["account_type"], ["id"])
    op.add_column("users", sa.Column("account_type", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "users", "account_types", ["account_type"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="foreignkey")
    op.drop_column("users", "account_type")
    op.drop_constraint(None, "business", type_="foreignkey")
    op.drop_column("business", "account_type")
    op.drop_table("accounts")
    # ### end Alembic commands ###
