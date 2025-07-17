rice_orders = [
    'pishori', 'indian', 'sindano', 'basmat',
    'indian', 'thailand', 'indian'
]
ready_rice = []

print("⁜ The store has run out of 'indian' rice.\n")

# Remove all 'indian' orders
while 'indian' in rice_orders:
    rice_orders.remove('indian')

# Process available rice orders
while rice_orders:
    current_order = rice_orders.pop(0)
    print(f"I have prepared your {current_order} rice.")
    ready_rice.append(current_order)

# Final list of prepared rice orders
print("\n✓ The following rice orders have been prepared:")
for rice in ready_rice:
    print(f"- {rice}")
