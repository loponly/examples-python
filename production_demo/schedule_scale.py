import asyncio
import time
from restack_ai import Restack

async def main():

    client = Restack()

    workflow_id = f"{int(time.time() * 1000)}-ExampleWorkflow"
    await client.schedule_workflow(
        workflow_name="ExampleWorkflow",
        workflow_id=workflow_id,
    )

    exit(0)

def run_schedule_scale():
    asyncio.run(main())

if __name__ == "__main__":
    run_schedule_scale()