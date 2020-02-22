
# GraphQl implementation
from session.models import Session, UserModel
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene

class UserNode(DjangoObjectType):
    class Meta:
        model = UserModel
        filter_fields =['first_name', 'last_name']
        interfaces = (graphene.relay.Node,)

class UserMutation(graphene.relay.ClientIDMutation):
    class Input:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
    # the response after mutation
    user =  graphene.Field(UserNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, first_name,last_name):
        user = UserModel.objects.create(first_name=first_name, last_name=last_name)
        user.save()
        return UserMutation(user=user)


class SessionNode(DjangoObjectType):
    class Meta:
        model = Session
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'completed': ['exact'],
            'owner': ['exact'],
            'owner__first_name': ['exact', 'icontains'],
            'owner__last_name': ['exact', 'icontains']
        }
        interfaces = (graphene.relay.Node,)



class Query(graphene.ObjectType):
    session = graphene.relay.Node.Field(SessionNode)
    all_sessions = DjangoFilterConnectionField(SessionNode)
    user = graphene.relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

class Mutation(graphene.ObjectType):
    create_user = UserMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)