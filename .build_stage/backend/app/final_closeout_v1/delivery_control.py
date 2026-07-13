from pydantic import BaseModel, Field

class DeliveryControlItemV1(BaseModel):
    key: str
    ready: bool = True

class DeliveryControlV1(BaseModel):
    items: list[DeliveryControlItemV1] = Field(default_factory=list)

    @property
    def ready(self) -> bool:
        return all(item.ready for item in self.items)

class DeliveryControlBuilderV1:
    def build(self) -> DeliveryControlV1:
        return DeliveryControlV1(items=[
            DeliveryControlItemV1(key="backend_ready"),
            DeliveryControlItemV1(key="tests_green"),
            DeliveryControlItemV1(key="release_metadata_ready"),
            DeliveryControlItemV1(key="package_plan_ready"),
            DeliveryControlItemV1(key="post_release_plan_ready"),
        ])
