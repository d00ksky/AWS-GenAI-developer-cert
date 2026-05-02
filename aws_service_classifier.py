from typing import Any


Service = dict[str, Any]


def filter_services_by_category(
    services: list[Service],
    category: str,
) -> list[Service]:
    # zwróć tylko te usługi, które mają daną kategorię
    service_with_category = []
    for service in services:
        if service["category"] == category:
            service_with_category.append(service)
    return service_with_category


def get_cost_related_services(services: list[Service]) -> list[Service]:
    # - category == "cost"
    # - albo "cost" znajduje się w risk
    cost_related_service = []
    for service in services:
        if service["category"] == "cost" or "cost" in service["risk"]:
            cost_related_service.append(service)
    return cost_related_service
    

def sort_services_by_name(services: list[Service]) -> list[Service]:
    # posortuj usługi alfabetycznie po name
    return sorted(services, key = lambda service: service["name"])


def print_services(title: str, services: list[Service]) -> None:
    # 1. wypisz tytuł
    # 2. dla każdej usługi wypisz "- NAME: RISK"
    print(f"\n{title}")
    for service in services:
        print(f"- {service["name"]}: {service["risk"]}")


def main() -> None:
    services: list[Service] = [
        {"name": "S3", "category": "storage", "risk": "data exposure"},
        {"name": "IAM", "category": "security", "risk": "over-permission"},
        {"name": "CloudWatch", "category": "monitoring", "risk": "missing logs"},
        {"name": "AWS Budgets", "category": "cost", "risk": "unexpected spend"},
        {"name": "Amazon Bedrock", "category": "genai", "risk": "token cost"},
    ]

    security_services = filter_services_by_category(services, "security")
    cost_services = get_cost_related_services(services)
    sorted_services = sort_services_by_name(services)

    print_services("Security-related services:", security_services)
    print_services("Cost-related services:", cost_services)

    print("\nAll services sorted by name:")
    # TODO: wypisz same nazwy usług z sorted_services
    for service in sorted_services:
        print(service["name"])


if __name__ == "__main__":
    main()
    
    
# Expected output

# Security-related services:
# - IAM: over-permission

# Cost-related services:
# - AWS Budgets: unexpected spend
# - Amazon Bedrock: token cost

# All services sorted by name:
# - Amazon Bedrock
# - AWS Budgets
# - CloudWatch
# - IAM
# - S3