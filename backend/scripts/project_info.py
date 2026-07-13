from app.v11_operations.project_info import ProjectInfoBuilderV11

if __name__ == "__main__":
    info = ProjectInfoBuilderV11().build()
    print(info.model_dump_json(indent=2))
