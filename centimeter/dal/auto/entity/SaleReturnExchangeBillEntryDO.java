package com.tqmall.finance.auto.entity;
import lombok.Data;

/**
 * 
 * 销售退换货关联商品明细
 * 
 **/

@Data
public class SaleReturnExchangeBillEntryDO {

	/****/
	private Integer id;

	/**操作人ID**/
	private Integer creator;

	/**创建时间**/
	private java.util.Date gmtCreate;

	/**更新人**/
	private Integer modifier;

	/**更新时间**/
	private java.util.Date gmtModified;

	/**是否已删除**/
	private String isDeleted;

	/**单据ID**/
	private Integer billId;

	/**单据类型**/
	private Integer billTypeId;

	/**来源单据类型**/
	private Integer sourceBillTypeId;

	/**来源单据ID**/
	private Integer sourceBillId;

	/**来源单据分录ID**/
	private Integer sourceBillEntryId;

	/**分录状态**/
	private Integer billEntryStatus;

	/**主订单类型**/
	private Integer mainBillTypeId;

	/**主订单ID**/
	private Integer mainBillId;

	/**主订单号**/
	private String mainBillNo;

	/**发货仓库ID**/
	private Integer warehouseId;

	/**仓库名**/
	private String warehouseName;

	/**退货货仓库ID**/
	private Integer returnWarehouseId;

	/**退货仓库名**/
	private String returnWarehouseName;

	/**退货数量**/
	private Integer returnQty;

	/**订单商品id**/
	private Integer orderGoodsId;

	/**商品id**/
	private Integer goodsId;

	/**商品编码**/
	private String goodsSn;

	/**商品名称**/
	private String goodsName;

	/**商品规格**/
	private String goodsFormat;

	/**最小单位**/
	private String minMeasureUnit;

	/**应发数量**/
	private Integer sendQty;

	/**退货单价**/
	private java.math.BigDecimal returnPrice;

	/**退货金额**/
	private java.math.BigDecimal returnAmount;

	/**图片url地址**/
	private String cardUrl;

	/**批次码**/
	private String batchNo;

	/**实际退货数量**/
	private Integer realReturnNumber;

	/**适配车型**/
	private String adapterModels;


}
