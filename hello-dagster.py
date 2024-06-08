from typing import List
from dagster import asset, AssetExecutionContext, AssetIn, Definitions, define_asset_job, AssetSelection, ScheduleDefinition

@asset(key="my_fist_asset_key", group_name="get_started")
def my_first_asset(context: AssetExecutionContext):
    """
    Descrizione del primo asset.
    """
    print("Esempio di un print")
    context.log.info("Esempio di messaggio nei log")
    return[1,2,3]

@asset(ins={"upstream": AssetIn(key="my_fist_asset_key")}, group_name="get_started")
def my_second_asset(context: AssetExecutionContext, upstream: List):
    """
    This is our second asset
    """
    data = upstream + [4,5,6]
    context.log.info(f"Output data is: {data}")
    return data

@asset(ins={
    "fist_upstream": AssetIn(key="my_fist_asset_key"),
    "second_upstream": AssetIn(key="my_second_asset")
    }, 
    group_name="get_started"
)
def my_third_asset(
    context: AssetExecutionContext,
    fist_upstream: List,
    second_upstream: List
    ):
    """
    This is out third asset
    """
    data = {
        "first_asset": fist_upstream,
        "second_asset": second_upstream,
        "third_asset": second_upstream + [7,8,9] 
    } 
    context.log.info(f"Output data is: {data}")
    return data

defs = Definitions(
    assets = [my_first_asset, my_second_asset, my_third_asset],
    jobs = [
        define_asset_job (
            name = "hello_dagster_job",
            selection = AssetSelection.groups("get_started"),
        )
    ],
    schedules = [
        ScheduleDefinition(
            name = "hello_dagster_schedule",
            job_name = "hello_dagster_job",
            cron_schedule = "* * * * *"
        )
    ]    
)



