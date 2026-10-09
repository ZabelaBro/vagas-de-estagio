import os
import ast

def check_file_exists(path):
    if not os.path.exists(path):
        print(f"❌ {path} não encontrado.")
        return False
    print(f"✅ {path} encontrado.")
    return True

def check_class_in_file(path, class_name):
    with open(path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    if class_name in classes:
        print(f"✅ Classe {class_name} encontrada em {path}.")
        return True
    print(f"❌ Classe {class_name} não encontrada em {path}.")
    return False

def check_inheritance(path, class_name, parent_name):
    with open(path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            bases = [b.id for b in node.bases if isinstance(b, ast.Name)]
            if parent_name in bases:
                print(f"✅ Herança {class_name}({parent_name}) encontrada em {path}.")
                return True
    print(f"❌ Herança {class_name}({parent_name}) não encontrada em {path}.")
    return False

def run_checks():
    print("Iniciando verificações...")
    checks = 0
    passed = 0

    def run_check(fn, *args):
        nonlocal checks, passed
        checks += 1
        if fn(*args):
            passed += 1

    run_check(check_file_exists, "app/__init__.py")
    run_check(check_file_exists, "app/data/empresas_mock.py")
    run_check(check_file_exists, "app/data/vagas_mock.py")
    run_check(check_file_exists, "app/models/empresa.py")
    run_check(check_file_exists, "app/models/vaga.py")
    run_check(check_file_exists, "app/controllers/empresas_controller.py")
    run_check(check_file_exists, "app/controllers/vagas_controller.py")
    run_check(check_file_exists, "app/routes/empresas_routes.py")
    run_check(check_file_exists, "app/routes/vagas_routes.py")
    run_check(check_class_in_file, "app/models/vaga.py", "Vaga")
    run_check(check_class_in_file, "app/models/vaga.py", "VagaPresencial")
    run_check(check_class_in_file, "app/models/vaga.py", "VagaRemota")
    run_check(check_inheritance, "app/models/vaga.py", "VagaPresencial", "Vaga")

    print(f"\nResultado: {passed}/{checks} testes passaram.")
    if passed == checks:
        print("Tudo certo! Pode entregar.")
    else:
        print("Alguns testes falharam. Revise o código.")

if __name__ == "__main__":
    run_checks()

