import os

# JobRad custom view pattern
CONTRACT_VIEW_PATTERN: str = "report_contract_document_body_%"

# Default is False, set UPGRADE_SKIP_JOBRAD_VIEWS=1 or assign True to enable skipping
skip_views: bool = os.getenv("UPGRADE_SKIP_JOBRAD_VIEWS", "0").lower() in ("1", "true", "yes", "on")
