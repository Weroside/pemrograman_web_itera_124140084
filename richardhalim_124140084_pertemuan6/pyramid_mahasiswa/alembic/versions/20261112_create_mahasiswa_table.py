from alembic import op
import sqlalchemy as sa

revision = "paw6_01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "mahasiswa",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nim", sa.Text(), nullable=False, unique=True),
        sa.Column("nama", sa.Text(), nullable=False),
        sa.Column("jurusan", sa.Text(), nullable=False),
    )


def downgrade():
    op.drop_table("mahasiswa")
