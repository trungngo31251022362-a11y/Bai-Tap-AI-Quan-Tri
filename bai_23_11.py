from sklearn.linear_model import LinearRegression
hours = np.array([6, 8, 10, 12, 14, 16, 18, 20, 22]).reshape(-1, 1)
demand = np.array([10, 85, 40, 95, 30, 70, 110, 50, 15]) 
model = LinearRegression().fit(hours, demand)
predicted_19h = model.predict([[19]])
print(f"Nhu cầu dự báo lúc 19:00 là: {predicted_19h[0]:.2f} đơn hàng")
