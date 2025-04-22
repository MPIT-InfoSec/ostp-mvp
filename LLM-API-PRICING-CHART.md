# 🧮 LLM Cost Breakdown (INR ₹ per JD)

This document outlines the cost of generating **one Job Description (JD)** using different OpenAI models, assuming:

- **Input tokens**: 200  
- **Output tokens**: 600  
- **Exchange rate**: $1 ≈ ₹83

---

## 🔝 Key Models to Compare

| Model          | Input $/M | Output $/M | Cost per JD (USD) | Cost per JD (INR) | Notes              |
|----------------|-----------|------------|-------------------|-------------------|--------------------|
| gpt-4.1        | $2.00     | $8.00      | $0.0520           | ₹4.32             | Smartest           |
| gpt-4.1-mini   | $0.40     | $1.60      | $0.0104           | ₹0.86             | Balanced           |
| gpt-4.1-nano   | $0.10     | $0.40      | $0.0026           | ₹0.22             | Fast + cheap       |
| gpt-4o         | $2.50     | $10.00     | $0.0650           | ₹5.40             | Multimodal capable |
| gpt-4o-mini    | $0.15     | $0.60      | $0.0039           | ₹0.32             | Good value         |
| gpt-3.5-turbo  | $0.0005   | $0.0015    | $0.0011           | ₹0.09             | Still the cheapest |

---

## 📊 Cost Comparison Summary (INR per JD)

| Model           | ₹ / JD  |
|------------------|---------|
| gpt-3.5-turbo     | ₹0.09   |
| gpt-4.1-nano      | ₹0.22   |
| gpt-4o-mini       | ₹0.32   |
| gpt-4.1-mini      | ₹0.86   |
| gpt-4.1           | ₹4.32   |
| gpt-4o            | ₹5.40   |

---

💡 *These numbers help you make cost-effective decisions depending on JD volume and formatting needs.*

---

# 💰 Fine-Tuning Costs for GPT-4.1 Mini

This table summarizes the costs associated with fine-tuning and using a custom GPT-4.1 Mini model. Prices are shown per **1 million tokens**, with approximate conversion to Indian Rupees (₹) at an exchange rate of **$1 ≈ ₹83**.

---

| Action            | Price (USD / 1M tokens) | INR (approx) |
|-------------------|--------------------------|---------------|
| Training          | $5.00                    | ₹415          |
| Inference Input   | $0.80                    | ₹66           |
| Inference Output  | $3.20                    | ₹266          |

---

💡 *Training cost is one-time, but inference cost applies every time you use the fine-tuned model in production.*