package com;
import java.util.HashMap;
import java.util.Map;

import org.junit.Test;

public class MyTest {
	
	@Test
	public void getResult()
	{
		
		long startTime = System.currentTimeMillis();
//		String url = "http://117.136.129.14:5901/CMNBDC/gis/GetMapDataBySG2";
//		String url = "http://10.254.201.201:8088/RedisServer/Hbase/GetData";
//		String url = "http://localhost:8080/WebPlatForm/Gis/MyTest";
//		String url = "http://117.136.129.17:5901/WebPlatForm/SixDimensions/GetSixDimensionsData";
//		String url = "http://10.254.201.218:8080/WebPlatForm/cell/G20CGIinfoGP";
//		String url = "http://10.254.201.218:8080/WebPlatForm/Gis/GetG20DataForLevel";
		String url = "http://10.254.201.218:8080/WebPlatForm/SixDimensions/GetSixDimensionsData";
//		String url = "http://10.254.201.218:8080/WebPlatForm/cell/KPITest";
//		String url = "http://10.254.201.218:8080/WebPlatForm/constant/Sixdimensionindex";
		
		Map<String, String> params = new HashMap<String, String>();
//		params.put("startline", "20");
//		params.put("stopline", "30");
//		params.put("type","1");
//		params.put("param","eu0113");
		
		params.put("region_type", "province");
		params.put("region_name", "北京");
		params.put("search_time","09");
		
//		params.put("regiontypes","1,2");
		String result = HttpClientUtil.invokeGet(url, params,  "UTF-8", 10000, 10000);
		System.out.println("result="+result);
		//HttpClientUtil.invokePost(get_payjsp_url, params, "UTF-8", 5000, 5000);
		long endTime = System.currentTimeMillis();
		System.out.println("共耗时="+(endTime-startTime)+"毫秒");
	}
}
