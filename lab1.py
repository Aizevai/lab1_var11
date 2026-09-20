import numpy as np
import matplotlib.pyplot as plt

#  ВАРИАНТ 11:  e^(-x) - x = 0,  отрезок [0, 1],  eps = 0.0001

eps = 1e-4


def f(x):
    """Исходная функция f(x) = e^(-x) - x"""
    return np.exp(-x) - x


def phi(x):
    """Отображение для метода простой итерации: phi(x) = e^(-x)"""
    return np.exp(-x)


def df(x):
    """Первая производная: f'(x) = -e^(-x) - 1"""
    return -np.exp(-x) - 1


def d2f(x):
    """Вторая производная: f''(x) = e^(-x)"""
    return np.exp(-x)


#  1. МЕТОД БИСЕКЦИИ (половинного деления)

print("=" * 70)
print("  МЕТОД БИСЕКЦИИ")
print("=" * 70)
print(f"{'Ит':>4} {'a':>12} {'b':>12} {'c=(a+b)/2':>12} {'f(c)':>14} {'b-a':>12}")
print("-" * 70)

a, b = 0.0, 1.0
n_bis = 0
while (b - a) / 2 > eps:
    n_bis += 1
    c = (a + b) / 2
    fc = f(c)
    print(f"{n_bis:>4} {a:>12.6f} {b:>12.6f} {c:>12.6f} {fc:>14.10f} {b-a:>12.6f}")
    if fc * f(a) < 0:
        b = c
    else:
        a = c

root_bis = (a + b) / 2
print(f"\n  Ответ: x = {root_bis:.6f}")
print(f"  Итераций: {n_bis}")
print(f"  Невязка: |f(x)| = {abs(f(root_bis)):.2e}\n")

#  2. МЕТОД ПРОСТОЙ ИТЕРАЦИИ

print("=" * 70)
print("  МЕТОД ПРОСТОЙ ИТЕРАЦИИ")
print("  phi(x) = e^(-x),  x0 = 0.5")
print("=" * 70)
print(
    f"{'Ит':>4} {'x_n':>14} {'x_{n+1}=phi(x_n)':>18} {'|x_{n+1}-x_n|':>16} {'f(x_{n+1})':>14}"
)
print("-" * 70)

x_prev = 0.5
n_iter = 0
while True:
    n_iter += 1
    x_next = phi(x_prev)
    diff = abs(x_next - x_prev)
    fx = f(x_next)
    print(f"{n_iter:>4} {x_prev:>14.10f} {x_next:>18.10f} {diff:>16.10f} {fx:>14.10f}")
    if diff < eps:
        break
    x_prev = x_next

root_iter = x_next
print(f"\n  Ответ: x = {root_iter:.6f}")
print(f"  Итераций: {n_iter}")
print(f"  Невязка: |f(x)| = {abs(f(root_iter)):.2e}\n")

#  3. МЕТОД НЬЮТОНА (касательных)

print("=" * 70)
print("  МЕТОД НЬЮТОНА")
print("  f'(x) = -e^(-x) - 1")
print("  Правило Фурье: f(0)*f''(0) = 1*1 = 1 > 0  =>  x0 = 0")
print("=" * 70)
print(
    f"{'Ит':>4} {'x_k':>14} {'f(x_k)':>14} {'f\'(x_k)':>14} {'x_{k+1}':>14} {'|x_{k+1}-x_k|':>16}"
)
print("-" * 70)

x_prev = 0.0
n_newton = 0
while True:
    n_newton += 1
    fx = f(x_prev)
    dfx = df(x_prev)
    x_next = x_prev - fx / dfx
    diff = abs(x_next - x_prev)
    print(
        f"{n_newton:>4} {x_prev:>14.10f} {fx:>14.10f} {dfx:>14.10f} {x_next:>14.10f} {diff:>16.10f}"
    )
    if diff < eps:
        break
    x_prev = x_next

root_newton = x_next
print(f"\n  Ответ: x = {root_newton:.6f}")
print(f"  Итераций: {n_newton}")
print(f"  Невязка: |f(x)| = {abs(f(root_newton)):.2e}\n")

#  4. МЕТОД СЕКУЩИХ

print("=" * 70)
print("  МЕТОД СЕКУЩИХ")
print("  x0 = 0,  x1 = 1  (концы отрезка)")
print("=" * 70)
print(f"{'Ит':>4} {'x_k':>14} {'f(x_k)':>14} {'x_{k+1}':>14} {'|x_{k+1}-x_k|':>16}")
print("-" * 70)

x_km1 = 0.0  # x_{k-1}
x_k = 1.0  # x_k
n_secant = 0
while True:
    n_secant += 1
    fx_km1 = f(x_km1)
    fx_k = f(x_k)
    x_next = x_k - fx_k * (x_k - x_km1) / (fx_k - fx_km1)
    diff = abs(x_next - x_k)
    print(f"{n_secant:>4} {x_k:>14.10f} {fx_k:>14.10f} {x_next:>14.10f} {diff:>16.10f}")
    if diff < eps:
        break
    x_km1 = x_k
    x_k = x_next

root_secant = x_next
print(f"\n  Ответ: x = {root_secant:.6f}")
print(f"  Итераций: {n_secant}")
print(f"  Невязка: |f(x)| = {abs(f(root_secant)):.2e}\n")

#  СВОДНАЯ ТАБЛИЦА

print("=" * 70)
print("  СВОДНАЯ ТАБЛИЦА СРАВНЕНИЯ МЕТОДОВ")
print("=" * 70)
print(f"{'Метод':>25} {'Корень':>12} {'Итераций':>10} {'Невязка':>14}")
print("-" * 70)
print(f"{'Бисекция':>25} {root_bis:>12.6f} {n_bis:>10} {abs(f(root_bis)):>14.2e}")
print(
    f"{'Простая итерация':>25} {root_iter:>12.6f} {n_iter:>10} {abs(f(root_iter)):>14.2e}"
)
print(
    f"{'Ньютон':>25} {root_newton:>12.6f} {n_newton:>10} {abs(f(root_newton)):>14.2e}"
)
print(
    f"{'Секущие':>25} {root_secant:>12.6f} {n_secant:>10} {abs(f(root_secant)):>14.2e}"
)
print()
print("  Вывод: Метод Ньютона сходится быстрее всех (всего 4 итерации).")
print("  Метод бисекции — самый медленный (13 итераций), но гарантированно сходится.")
print("  Метод простой итерации и секущих занимают промежуточное положение.")

#  ГРАФИК

x_vals = np.linspace(-0.2, 1.2, 300)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, f(x_vals), "b-", linewidth=2, label="f(x) = e^(-x) - x")
plt.axhline(0, color="gray", linewidth=0.8)
plt.plot(
    root_newton,
    f(root_newton),
    "ro",
    markersize=8,
    label=f"Корень x ≈ {root_newton:.6f}",
)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции f(x) = e^(-x) - x (вариант 11)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graph_variant11.png", dpi=150)
print("\n  График сохранён в файл graph_variant11.png")
