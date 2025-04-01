import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

data = {
    'X': [3, 20, 50, 70, 100],
    'No Privacy Protection': [7704.333333333333, 4960.9, 5116.54, 4575.228571428572, 4958.49],
    'Paillier': [7704.333333333333, 4960.9, 5116.54, 4575.228571428572, 4958.49],
    'Shamir': [7704.333333333333, 4960.9, -6.071238526399472e+21, 9.548915671708226e+40, -2.1188765284839826e+75],
    'Differential Privacy': [7704.333333333333, 6044.4421942307445, 5160.538294182562, 4575.228571428572, 5041.6185071540485]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['X'], df['No Privacy Protection'], label='No Privacy Protection', color='red')
plt.plot(df['X'], df['Paillier'], label='Paillier', color='blue')
plt.plot(df['X'], df['Shamir'], label='Shamir', color='green')
plt.plot(df['X'], df['Differential Privacy'], label='Differential Privacy', color='purple')
plt.title('Average')
plt.xlabel('The number of random integers')
plt.ylabel('Average')
plt.legend()

# Save the plot to a PDF file
with PdfPages('graph.pdf') as pdf:
    pdf.savefig()

plt.close()
