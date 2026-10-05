import typer


def main(generator: str):
    print(f"Generator: {generator}")


if __name__ == "__main__":
    typer.run(main)
