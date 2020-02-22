
# GraphQl implementation
from session.models import Session, UserModel
from graphene_django import DjangoObjectType
import graphene

class UserObject(DjangoObjectType):
    class Meta:
        model = UserModel


class SessionObject(DjangoObjectType):
    class Meta:
        model = Session


class Query(graphene.ObjectType):
    user = graphene.Field(UserObject, id=graphene.Int(), first_name=graphene.String())
    session = graphene.Field(SessionObject, id=graphene.Int(), name=graphene.String())
    users = graphene.List(UserObject)
    sessions = graphene.List(SessionObject)

    def resolve_users(self, info):
        return UserModel.objects.all()
    
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        name =  kwargs.get('first_name')
        if id is not None:
            return UserModel.objects.get(pk=id)

        if name is not None:
            return UserModel.objects.get(first_name=name)
    
        return None

    def resolve_sessions(self, info):
        return Session.objects.all()

    def resolve_session(self, info, **kwargs):
        id = kwargs.get('id')
        owner =  kwargs.get('owner')
        if id is not None:
            return Session.objects.get(pk=id)

        if owner is not None:
            return Session.objects.get(owner=owner)
            
        return None

schema = graphene.Schema(query=Query)