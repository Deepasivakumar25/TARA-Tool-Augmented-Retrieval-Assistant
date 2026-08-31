tokenizer = AutoTokenizer.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct"
)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct"
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)
