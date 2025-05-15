from typing import Protocol

from apps.seller.clients.open_ai import OpenApiClient


class BotRulesV1:
    base_rules = """
    You are a virtual car salesman for a online platform called Kavak. \
    Be cordial at all times. \
    You must adapt to the customer language \
    customers sometimes can fail writing the cards brands or car names \
    Offer recommendations if customers are undecided  \
    Based on customer preferences, you can offer financing plans based on the down payment, the price of the vehicle, a 10% interest rate, and financing terms between 3 and 6 years.\
    Not create any new car or promotion \
    give at least 4 car options when is possible \ 
    Be concise and do not repeat the same information many times. \
    """

    def get_cars_from_csv(self):
        with open("apps/seller/services/sample_caso_ai_engineer.csv", encoding='UTF-8') as file:
            cars = file.read()
        return cars

    def get_kavak_value(self):
        with open("apps/seller/services/value", encoding='UTF-8') as f:
            value = f.read()
        return value

    def get_rules(self):
        return f"""{self.base_rules}
            Below is your list of cars always use this list to any query\
            {self.get_cars_from_csv()}
            When is possible talk about the adventages of using kavak listed here:  \
            {self.get_kavak_value()}
        """


user_contexts = {}


class Rule(Protocol):
    def get_rules(self):
        pass


class Session:
    context = []

    def __init__(self, rules: Rule = BotRulesV1()):
        self.context.append({'role': 'system', 'content': f"""{rules.get_rules()}"""})

    def new_msg(self, msg, agent):
        self.context.append({'role': 'user', 'content': f"{msg}"})
        response = agent.fetch_messages(self.context, temperature=0.7)
        self.context.append({'role': 'assistant', 'content': f"{response}"})
        return response


class SellerBotService:

    @classmethod
    def get_user_session(cls, usr_id):
        try:
            session = user_contexts[usr_id]
        except KeyError:
            user_contexts[usr_id] = Session()
            session = user_contexts[usr_id]
        return session

    @classmethod
    def get_response(cls, msg, usr_id):
        agent = OpenApiClient()
        session = cls.get_user_session(usr_id)
        return session.new_msg(msg, agent)
