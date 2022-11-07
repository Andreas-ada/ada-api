from fastapi import APIRouter
from typing import Dict

router = APIRouter(prefix="", tags=["example"])


@router.post("/example")
async def example_post(example_dict: Dict):
	print(example_dict)
	
	return {
		"SUCCESSFUL": True
	}
