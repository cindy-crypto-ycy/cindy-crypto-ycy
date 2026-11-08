# 主页维护说明

这是 `cindy-crypto-ycy/cindy-crypto-ycy` 的 GitHub 个人主页介绍。根目录的 `readme.md` 是主页入口，`assets/` 保存动画素材。

## 发布

将本次文件提交并推送到这个同名公开仓库的默认分支，GitHub 就会在个人主页显示介绍。无需部署网站，也无需启用 GitHub Actions。

如果仓库不是公开状态，需要先确认是否要公开它。发布后访问：

https://github.com/cindy-crypto-ycy

## 修改介绍

- 在 `readme.md` 修改个人介绍、技能与业务内容。
- 展示名目前为 **Cindy**。动画中的名字在 `scripts/generate_assets.py` 中修改。
- 尚未填写未经确认的具体工具栈、工作年限、公司信息或业绩数据。
- 按当前要求暂不生成或更换头像。修改 README 不会修改 GitHub 账号头像。

## 修改动画

使用 Python 3 运行，无需安装第三方依赖：

```powershell
python scripts/generate_assets.py
```

脚本重新生成六张 SVG：

| 文件 | 动效 |
| --- | --- |
| `assets/hero.svg` | 雷达轨道旋转、终端光标闪烁 |
| `assets/performance.svg` | 性能曲线绘制 |
| `assets/api.svg` | 请求、断言、响应之间的数据流 |
| `assets/automation.svg` | 扫描光效与状态灯呼吸 |
| `assets/ai-workflows.svg` | AI 工作节点脉冲与数据流 |
| `assets/workflow.svg` | 五阶段测试流程动画 |

动画使用 SVG 内嵌 CSS，无 JavaScript、外部字体或外部图片服务。动画是装饰性示意，不代表实时运行结果或性能数据。系统开启减少动态效果时，动画会静止，内容仍然可见。

GitHub README 会过滤脚本与部分 HTML 样式，因此动画放在独立 SVG 图片中。GitHub 图片缓存可能造成更新延迟；发布后应检查个人主页实际渲染。本地 `.preview/` 是近似 GitHub 排版的预览和检查文件，不会随仓库提交。
