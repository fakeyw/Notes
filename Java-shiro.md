## Shiro

一种适用于java语言的权限安全管理架构

但是架构还是挺简单的

大致思路是：

应用逻辑接入`SecurityManage`r时

会抽象出一个 `Subject` ，就跟用户似的

像访问网页一样，会产生一个时间敏感的`Session` 

在鉴权后由最后一层 -- `Realm` （DAO）来直接接触获取各种数据

中间为了保密之类的，在层间添了一些加密手段



所以说 这tm跟访问网页有啥区别吗？。。。

跟我之前blog的Auth模块功能差不多



## JFinal

比起Shiro，这个就麻烦点了。

