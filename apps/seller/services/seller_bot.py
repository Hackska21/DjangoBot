from apps.seller.clients.open_ai import OpenApiClient
from apps.seller.models import UserSessionModel
from apps.seller.services.rules.rulesv1 import BotRulesV1, Rule


class UserChatSession:
    context = []
    session_model = None

    def get_user_session(self, usr_id, version):
        self.session_model, _ = UserSessionModel.objects.get_or_create(
            user_id=usr_id, version=version
        )
        self.context = self.session_model.context_data

    def __init__(self, user_id, rules: Rule = BotRulesV1()):
        self.get_user_session(user_id, rules.version)
        if not self.context:
            self.context.append({'role': 'system', 'content': f"""{rules.get_rules()}"""})

    def new_msg(self, msg, agent: OpenApiClient):
        self.context.append({'role': 'user', 'content': f"{msg}"})
        response = agent.fetch_messages(self.context, temperature=0.7)
        self.context.append({'role': 'assistant', 'content': f"{response}"})
        self.update_model()
        return response

    def update_model(self):
        self.session_model.context_data = self.context
        self.session_model.save(update_fields=['context_data'])


class SellerBotService:

    @classmethod
    def get_response(cls, msg, usr_id):
        agent = OpenApiClient()
        session = UserChatSession(user_id=usr_id)
        return session.new_msg(msg, agent)
