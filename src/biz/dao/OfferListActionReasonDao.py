__author__ = 'chenjinlong'
from dal.mapper.OfferListActionReasonMapper import OfferListActionReasonMapper
class OfferListActionReasonDao(object):
    offerListActionReasonMapper = OfferListActionReasonMapper()

    def getByOfferListIdList(self, offerListIdList):
        if len(offerListIdList) == 0:
            return []
        offerListActionReasonDOList = self.offerListActionReasonMapper.selectByOfferListIdList(offerListIdList)
        return offerListActionReasonDOList