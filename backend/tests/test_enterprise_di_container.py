from app.enterprise_v1.di_container import DIContainerV1

def test_di_container():
    c = DIContainerV1()
    c.register("x", 1)
    assert c.resolve("x") == 1
