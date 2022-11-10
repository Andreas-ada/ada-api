from fastapi import APIRouter
from typing import Dict

router = APIRouter(prefix="", tags=["example"])


@router.post("/example")
async def example_post(example_dict: Dict):
	print(example_dict)
	
	return {
		"SUCCESSFUL": True
	}



@router.get("/example/{test_id}")
async def example_get(test_id: str):
	return {
		"test_id":test_id,
		"SUCCESSFUL": True
	}
