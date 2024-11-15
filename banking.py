from abc import ABC,abstractmethod


class Strategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

# Concrete Strategy 1: 일반 할인 전략
class NormalMember(Strategy):
    def apply_discount(self, amount):
        m = amount * 0.020
        # print(f'회원 혜택: {m}원')
        return amount + m

# Concrete Strategy 2: 10% 회원 혜택 전략
class PremiumMember(Strategy):
    def apply_discount(self, amount):
        m = amount * 0.040
        # print(f'회원 혜택: {m}원')
        return amount + m

# Concrete Strategy 3: 20% 시즌 혜택 전략
class LoyalMember(Strategy):
    def apply_discount(self, amount):
        m = amount * 0.060
        # print(f'회원 혜택: {m}원')
        return amount + m

# Context: 쇼핑 카트 클래스
class wallet:
    def __init__(self, balance, strategy:Strategy):
        self.strategy = strategy
        self.balance = balance

    def calculate_total(self):
        # print(f'총 금액: {self.balance}원')
        return self.strategy.apply_discount(self.balance)

    def set_strategy(self, strategy):
        self.strategy = strategy

# 클라이언트 코드
backbook = wallet(10000, NormalMember())  # 기본적으로 혜택이 없음


# 혜택이 적용되지 않은 상태에서 총 금액 계산
print('== NormalMember ==')
total = backbook.calculate_total()
print(f'혜택 적용 금액: {total}원\n')

# 회원 혜택을 적용
print('== PremiumMember==')
backbook.set_strategy(PremiumMember())
total = backbook.calculate_total()
print(f'혜택 적용 금액: {total}원\n')

# 시즌 혜택을 적용
print('== SeasonDiscount ==')
backbook.set_strategy(LoyalMember())
total = backbook.calculate_total()
print(f'혜택 적용 금액: {total}원')