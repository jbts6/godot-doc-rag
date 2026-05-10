#!/usr/bin/env python3
"""
在 Windows 上运行，将 embedding 模型导出为 ONNX。
导出完成后将 onnx_model/ 目录复制到 Mac。
"""

from optimum.onnxruntime import ORTModelForFeatureExtraction
from transformers import AutoTokenizer

EMBED_MODEL = "sentence-transformers/all-mpnet-base-v2"
OUTPUT_DIR = "onnx_model"

print(f"导出 {EMBED_MODEL} → {OUTPUT_DIR}/")

model = ORTModelForFeatureExtraction.from_pretrained(EMBED_MODEL, export=True)
model.save_pretrained(OUTPUT_DIR)

tokenizer = AutoTokenizer.from_pretrained(EMBED_MODEL)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"\n导出完成! 将 {OUTPUT_DIR}/ 目录复制到 Mac。")
