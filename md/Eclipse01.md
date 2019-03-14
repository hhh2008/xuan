Eclipse中添加文档注释快捷键
例如：

/**
  * @param  
  * @return

  */

快捷键为：ALT + SHIFT +J

想更换为其他的快捷键：

Window-->Preferences-->General-->Keys;找到"add javadoc comment"更改自己喜欢的快捷键。

另外如果觉得注释也不爽时也可以改改，修改的方法有两种：

1.直接在eclipse给的模板下进行修改

2.自己编写一个xml文档导入进去

那就来先说说第一种方法吧：

打开eclipse

Window-->Preferences-->Java-->Code Style --> Code Templates --> Comments --> types --> Edit

/**   
*    
* 项目名称：${project_name}   
* 类名称：${type_name}   
* 类描述：   
* 创建人：${user}   
* 创建时间：${date} ${time}   
* 修改人：${user}   
* 修改时间：${date} ${time}   
* 修改备注：   
* @version    
*    
*/

第二种方法是：

点击右边的import按钮选择你写好的模板.xml文件

下面是一个注释行模板codetemplates.xml，可以直接导入使用。贴出源码供大家参考一下

<?xml version="1.0" encoding="UTF-8"?>
<templates>

<template autoinsert="false"
context="constructorcomment_context"
deleted="false" description="Comment for created constructors"
enabled="true"
id="org.eclipse.jdt.ui.text.codetemplates.constructorcomment"
name="constructorcomment">
/**
* 创建一个新的实例 ${enclosing_type}.
*
* ${tags}
*/
</template>

<template autoinsert="true"
context="settercomment_context"
deleted="false"
description="Comment for setter method"
enabled="true" id="org.eclipse.jdt.ui.text.codetemplates.settercomment"
name="settercomment">
/**
* @param ${param} the ${bare_field_name} to set
*/
</template>

<template autoinsert="false"
context="methodcomment_context"
deleted="false"
description="Comment for non-overriding methods"
enabled="true" id="org.eclipse.jdt.ui.text.codetemplates.methodcomment"
name="methodcomment">
/**
* ${enclosing_method}(这里用一句话描述这个方法的作用)
* TODO(这里描述这个方法适用条件 – 可选)
* TODO(这里描述这个方法的执行流程 – 可选)
* TODO(这里描述这个方法的使用方法 – 可选)
* TODO(这里描述这个方法的注意事项 – 可选)
* @param name
* @param @return 设定文件
* @return String DOM对象
* @Exception 异常对象
* @since CodingExample　Ver(编码范例查看) 1.1
*/
</template>

<template autoinsert="true"
context="delegatecomment_context"
deleted="false"
description="Comment for delegate methods"
enabled="true"
id="org.eclipse.jdt.ui.text.codetemplates.delegatecomment"
name="delegatecomment">
/**
* ${tags}
* ${see_to_target}
*/
</template>

<template autoinsert="false"
context="filecomment_context"
deleted="false"
description="Comment for created Java files"
enabled="true"
id="org.eclipse.jdt.ui.text.codetemplates.filecomment"
name="filecomment">
/**
* 文件名：${file_name}
*
* 版本信息：
* 日期：${date}
* Copyright 足下 Corporation ${year}
* 版权所有
*
*/
</template>

<template autoinsert="false"
context="gettercomment_context"
deleted="false"
description="Comment for getter method"
enabled="true"
id="org.eclipse.jdt.ui.text.codetemplates.gettercomment"
name="gettercomment">
/**
* ${bare_field_name}
*
* @return the ${bare_field_name}
* @since CodingExample Ver(编码范例查看) 1.0
*/
</template>

<template autoinsert="true"
context="overridecomment_context"
deleted="false"
description="Comment for overriding methods"
enabled="true"
id="org.eclipse.jdt.ui.text.codetemplates.overridecomment"
name="overridecomment">
/**
* (non-Javadoc)
* ${see_to_overridden}
*/
</template>

<template autoinsert="false"
context="fieldcomment_context"
deleted="false"
description="Comment for fields"
enabled="true"
id="org.eclipse.jdt.ui.text.codetemplates.fieldcomment"
name="fieldcomment">
/**
* ${field}:${todo}（用一句话描述这个变量表示什么）
*
* @since Ver 1.1
*/
</template>

<template autoinsert="false"
context="typecomment_context"
deleted="false"
description="Comment for created types"
enabled="true"
id="org.eclipse.jdt.ui.text.codetemplates.typecomment"
name="typecomment">
/**
*
* 项目名称：${project_name}
* 类名称：${type_name}
* 类描述：
* 创建人：${user}
* 创建时间：${date} ${time}
* 修改人：${user}
* 修改时间：${date} ${time}
* 修改备注：
* @version
*
*/</template>

</templates>