package com.tqmall.finance.auto.mapper;

import com.tqmall.finance.auto.entity.SaleReturnExchangeBillEntryDO;
import org.apache.ibatis.annotations.Param;
import java.util.List;
import java.util.Map;

/**
 * 
 * SaleReturnExchangeBillEntryMapper数据库操作接口类
 * 
 **/

public interface SaleReturnExchangeBillEntryMapper{


	/**
	 * 
	 * 删除（根据主键ID删除）
	 * 
	 **/
	Integer deleteByPrimaryKey ( @Param("id") Integer id );

	/**
	 * 
	 * 添加 （匹配有值的字段）
	 * 
	 **/
	Integer insertSelective( SaleReturnExchangeBillEntryDO record );

	/**
	 * 
	 * 查询（根据主键ID查询）
	 * 
	 **/
	SaleReturnExchangeBillEntryDO  selectByPrimaryKey ( @Param("id") Integer id );

	/**
	 * 
	 * 修改 （匹配有值的字段）
	 * 
	 **/
	Integer updateByPrimaryKeySelective( SaleReturnExchangeBillEntryDO record );

	/**
	 * 
	 * 批量添加
	 * 
	 **/
	Integer batchInsert ( @Param("saleReturnExchangeBillEntryDOList") List<SaleReturnExchangeBillEntryDO> saleReturnExchangeBillEntryDOList );

	/**
	 * 
	 * 动态条件查询总数目
	 * 
	 **/
	Integer countByBaseCondition ( Map<String,Object> map );

	/**
	 * 
	 * 动态条件查询（支持分页）
	 * 
	 **/
	List<SaleReturnExchangeBillEntryDO> selectByBaseConditionPageable ( Map<String,Object> map );

	/**
	 * 
	 * 批量更新
	 * 
	 **/
	Integer batchUpdateById ( @Param("saleReturnExchangeBillEntryDOList") List<SaleReturnExchangeBillEntryDO> saleReturnExchangeBillEntryDOList );

}