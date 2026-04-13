# 🔬 Substrate Ontology V6.0 Validation Suite
> **验证基底本体论V6.0核心预言：CMB低频截断、奥伯斯佯谬统一解释、夸克禁闭几何起源**  
> *论文: "The Geometric Origin of Propagation Limits: From Planck Scale to Cosmic Horizon" (Zhou, 2026)*  
> **✅ 审稿人可在120秒内完成全部验证 | 无需专业环境 | 仅需Python 3.8+**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19554502.svg)](https://doi.org/10.5281/zenodo.19554502)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 🌟 为什么这个仓库重要？
根据V6.0理论（Section 3.5.8）：
> *"CMB在<10 MHz频段应显著低于普朗克黑体谱——这是几何稀释截断的直接证据"*

本仓库提供**可重复、可证伪、可扩展**的验证路径：
- 📡 **CMB低频截断**：模拟1 MHz–1 THz频谱，突出<10 MHz截断
- 🌌 **奥伯斯佯谬统一**：对比"黑暗夜空"与"CMB微波背景"的同一机制
- ⚛️ **夸克禁闭验证**：计算强子化距离与色荷的定量关系

## ⚡ 120秒验证指南（审稿人专用）
```bash
# 1. 克隆仓库（10秒）
git clone https://github.com/yourusername/substrate-ontology-v6-validation.git
cd substrate-ontology-v6-validation

# 2. 安装依赖（30秒｜仅需3个轻量库）
pip install -r requirements.txt

# 3. 运行核心验证（80秒）
python cmb_simulation.py          # 生成CMB截断图（Fig 4论文对应）
python sky_brightness.py          # 生成奥伯斯佯谬对比图
python quark_confinement.py       # 生成夸克禁闭关系图

# 4. 查看结果
# 所有图表自动保存至 figures/ 目录
# 预期输出示例见 figures/ 预生成图
