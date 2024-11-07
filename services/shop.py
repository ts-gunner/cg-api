from sqlalchemy.orm import Session

from db.shop import RewardsBalance, RewardsBalanceBase
from models.common import APIResponse
from utils.logger import LoguruLogger


class ShopDataManager:
    def __init__(self, db: Session):
        self.db = db

    def get_balance_object(self, user_id: str) -> RewardsBalance:
        balance = self.db.query(RewardsBalance).filter(RewardsBalance.user_id == user_id).first()
        if not balance:
            balance = RewardsBalance(user_id=user_id)
            self.db.add(balance)
            self.db.commit()
        return balance


class ShopService:
    def __init__(self, db: Session):
        self.db = db
        self._logger = LoguruLogger.get_logger()
        self._dm = ShopDataManager(db)

    def get_shop_profile(self, user_id):
        obj = self._dm.get_balance_object(user_id)
        return APIResponse(data=RewardsBalanceBase.model_validate(obj))
