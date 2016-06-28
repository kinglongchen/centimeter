# -*- coding: utf-8 -*-
__author__ = 'chenjinlong'
from sqlalchemy import Column,SmallInteger,String,SmallInteger,DateTime,SmallInteger,DateTime,String,String,SmallInteger,SmallInteger,String,SmallInteger,SmallInteger,SmallInteger,SmallInteger,String,String,SmallInteger,SmallInteger,SmallInteger,SmallInteger,SmallInteger,String,String,String,SmallInteger,String,SmallInteger,String,Float,Float,Float,Float,Float,Float,Float,Float,String,DateTime,DateTime,DateTime,DateTime,String,Float,SmallInteger,Float,SmallInteger,String,String,String,SmallInteger,String,SmallInteger,String,String,String,SmallInteger,SmallInteger,SmallInteger,SmallInteger,SmallInteger,Float,String,String,SmallInteger,SmallInteger,SmallInteger,DateTime,DateTime,DateTime,DateTime,DateTime,DateTime,DateTime,DateTime,DateTime,DateTime,Float,Float,Float,SmallInteger,SmallInteger,SmallInteger,DateTime,DateTime
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
class OrderInfoDO(Base):

	# 表的名字:
	__tablename__ = 'venus_order_info'

	#是否已删除 N:未删除，Y:删除
	id=Column('id',SmallInteger,primary_key=True)
	#是否已删除 N:未删除，Y:删除
	isDeleted=Column('is_deleted',String(1))

	#创建人
	creator=Column('creator',SmallInteger)

	#创建时间
	gmtCreate=Column('gmt_create',DateTime)

	#修改人
	modifier=Column('modifier',SmallInteger)

	#修改时间
	gmtModified=Column('gmt_modified',DateTime)

	#订单编码
	orderSn=Column('order_sn',String(20))

	#外部商家订单编码
	externalOrderSn=Column('external_order_sn',String(20))

	#订单来源
	orderSourceType=Column('order_source_type',SmallInteger)

	#销售员id
	saleId=Column('sale_id',SmallInteger)

	#销售员名称
	saleName=Column('sale_name',String(128))

	#用户中心shop表的user_id,原来的名字user_id
	shopId=Column('shop_id',SmallInteger)

	#订单状态 -5 被拆单 -3 被合单 -2 删除 0 未确认 1 已确认 2 取消 3 无效
	orderStatus=Column('order_status',SmallInteger)

	#0 未发货 1 已发货
	shippingStatus=Column('shipping_status',SmallInteger)

	#付款状态 0 未付款 1 付款中 2 已付款
	payStatus=Column('pay_status',SmallInteger)

	#shop的门店名称
	companyName=Column('company_name',String(50))

	#收货人名称
	consignee=Column('consignee',String(60))

	#收货地址－乡村
	country=Column('country',SmallInteger)

	#收货地址－省
	province=Column('province',SmallInteger)

	#收货地址－城市
	city=Column('city',SmallInteger)

	#收货地址－区
	district=Column('district',SmallInteger)

	#收货地址－街道
	street=Column('street',SmallInteger)

	#收货地址－详细信息
	address=Column('address',String(255))

	#收货人手机号码
	mobile=Column('mobile',String(60))

	#订单备注 内部备注,例如小秘书、销售备注
	postscript=Column('postscript',String(1024))

	#发货方式
	shippingId=Column('shipping_id',SmallInteger)

	#发货方式名称
	shippingName=Column('shipping_name',String(120))

	#支付方式 暂时交易中心定义
	payId=Column('pay_id',SmallInteger)

	#支付名称
	payName=Column('pay_name',String(120))

	#商品金额
	goodsAmount=Column('goods_amount',Float)

	#运费
	shippingFee=Column('shipping_fee',Float)

	#线上支付的实际金额
	payFee=Column('pay_fee',Float)

	#
	moneyPaid=Column('money_paid',Float)

	#红包优惠
	bonus=Column('bonus',Float)

	#订单金额
	orderAmount=Column('order_amount',Float,default='0.00')

	#真实价格
	oriOrderAmount=Column('ori_order_amount',Float)

	#审计用订单金额
	auditAmount=Column('audit_amount',Float)

	#订单来源 云修|app
	referer=Column('referer',String(255))

	#下单时间
	addTime=Column('add_time',DateTime)

	#订单确认下推时间
	confirmTime=Column('confirm_time',DateTime)

	#订单支付时间
	payTime=Column('pay_time',DateTime)

	#订单发货时间
	shippingTime=Column('shipping_time',DateTime)

	#发票类型
	invType=Column('inv_type',String(60))

	#税 暂时无用
	tax=Column('tax',Float)

	#拆单合单使用父订单编号
	parentId=Column('parent_id',SmallInteger)

	#订单总折扣
	discount=Column('discount',Float)

	#发货仓库id
	warehouseId=Column('warehouse_id',SmallInteger)

	#业务备注 比如业务经理手机号, 拆单合单优惠等,下单界面填的备注
	businessNote=Column('business_note',String(255))

	#属性扩展字段
	attributes=Column('attributes',String(512))

	#交易状态, 参考订单中心OperateKeyEnum
	tradeStatus=Column('trade_status',String(10))

	#商家id
	sellerId=Column('seller_id',SmallInteger)

	#商家昵称
	sellerNick=Column('seller_nick',String(255))

	#用户类型：1门店、2普通用户
	userType=Column('user_type',SmallInteger)

	#订单标记，通过“,”分隔（BHD被合单、BCD被拆单、GJG改价格、GPS改配送、DYD第一单、XSYTH销售已提货）
	orderFlags=Column('order_flags',String(200))

	#支付商返回的流水号
	payNo=Column('pay_no',String(50))

	#扫描支付url
	payUrl=Column('pay_url',String(512))

	#城市站ID
	cityId=Column('city_id',SmallInteger)

	#uc里面的登陆操作帐户id
	accountId=Column('account_id',SmallInteger)

	#服务订单id
	orderServiceId=Column('order_service_id',SmallInteger)

	#计划状态 1-可出库, 2-部分缺货, 3-全部缺货, 4-可调拨
	planStatus=Column('plan_status',SmallInteger)

	#运算优先级,数量大优先级高
	planPriority=Column('plan_priority',SmallInteger)

	#拒收金额
	returnAmount=Column('return_amount',Float)

	#取消状态 先申请取消 通过后变成取消确认
	warehouseStatus=Column('warehouse_status',String(10))

	#出库单号
	deliveryNo=Column('delivery_no',String(20))

	#缺货标示 0:可预约 1：缺货
	stockoutType=Column('stockout_type',SmallInteger)

	#下推出库单状态 0-未下推, 1－已下推
	transferStatus=Column('transfer_status',SmallInteger)

	#到货确认状态 0 未到货，1 部分到货，2 全部到货
	arrivalStatus=Column('arrival_status',SmallInteger)

	#发货日期
	sendDate=Column('send_date',DateTime)

	#交货日期 包括拒收时间
	signDate=Column('sign_date',DateTime)

	#打印出库单时间
	printTime=Column('print_time',DateTime)

	#下推ERP时间
	pushdownTime=Column('pushdown_time',DateTime)

	#出库时间
	outWareTime=Column('out_ware_time',DateTime)

	#最后一次派送时间
	redispatchTime=Column('redispatch_time',DateTime)

	#退货入库日期
	returnInWareDate=Column('return_in_ware_date',DateTime)

	#收款日期
	receiveCashDate=Column('receive_cash_date',DateTime)

	#退款日期
	refundDate=Column('refund_date',DateTime)

	#核销时间
	gmtWriteOff=Column('gmt_write_off',DateTime)

	#核销金额
	writeOffAmount=Column('write_off_amount',Float)

	#实收总金额
	receiveAmount=Column('receive_amount',Float)

	#实退金额
	realReturnAmount=Column('real_return_amount',Float)

	#核销状态:1,已核销,0,未核销
	writeOffStatus=Column('write_off_status',SmallInteger)

	#财务收款方式(备注 1:现金收款,2:POS收款,3:银行转账,4:支付宝转账,5:在线收款（预付）)
	receiveType=Column('receive_type',SmallInteger)

	#打印状态 未打印  `已打印 错误列表
	printStatus=Column('print_status',SmallInteger)

	#预约时间
	appointmentTime=Column('appointment_time',DateTime)

	#可出库时间
	canOutWarehouseTime=Column('can_out_warehouse_time',DateTime)


