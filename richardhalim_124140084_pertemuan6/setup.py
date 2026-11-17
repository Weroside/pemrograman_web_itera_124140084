from setuptools import find_packages, setup

setup(
    name="pyramid-mahasiswa",
    version="1.0.0",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=["pyramid", "waitress", "SQLAlchemy", "alembic",
                      "psycopg2-binary"],
    entry_points={"paste.app_factory": ["main=pyramid_mahasiswa:main"]},
)
