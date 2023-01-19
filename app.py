from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from strawberry.schema import Schema
from strawberry.fastapi import GraphQLRouter
from api.query import Query
from api.mutation import Mutation
from api.utils.context import Context


def get_context():
    return Context()


schema = Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
async def root():
    return RedirectResponse(url="/graphql")
