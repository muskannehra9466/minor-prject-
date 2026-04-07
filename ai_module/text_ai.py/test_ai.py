from doubt_solver import solve_doubt
from pyq_fetcher import fetch_pyqs

# test doubt solver
question = input("Apna question likho: ")
answer = solve_doubt(question)

print("Answer:", answer)

# test PYQ
topic = input("Topic likho: ")
pyqs = fetch_pyqs(topic)

print("PYQs:")
for q in pyqs:
    print(q)
