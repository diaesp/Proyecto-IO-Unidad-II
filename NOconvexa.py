def f(x1, x2, y1, y2):
    
    return (x1 - 4)**2 + (x2 - 3)**2 + (y1 - 6)**2 + (y2 - 1)**2


def grad_f(x1, x2, y1, y2):
   
    grad_x1 = 2 * (x1 - 4)
    grad_x2 = 2 * (x2 - 3)
    grad_y1 = 2 * (y1 - 6)
    grad_y2 = 2 * (y2 - 1)
    return [grad_x1, grad_x2, grad_y1, grad_y2]


def g1(x1, x2):
    
    return x1**2 + x2**2 - 25


def g2(y1, y2):
   
    return y1**2 + y2**2 - 50


def projected_gradient_descent(initial_point, lr=0.1, tol=1e-6, max_iter=1000):
    
    x = initial_point[:] 
    history = []

    for _ in range(max_iter):
        grad = grad_f(x[0], x[1], x[2], x[3])
        
        x_new = [x[i] - lr * grad[i] for i in range(4)]

        
        if g1(x_new[0], x_new[1]) > 0:
            norm = (x_new[0]**2 + x_new[1]**2)**0.5
            x_new[0] = x_new[0] / norm * (25**0.5)
            x_new[1] = x_new[1] / norm * (25**0.5)

        
        if g2(x_new[2], x_new[3]) > 0:
            norm = (x_new[2]**2 + x_new[3]**2)**0.5
            x_new[2] = x_new[2] / norm * (50**0.5)
            x_new[3] = x_new[3] / norm * (50**0.5)

        
        history.append((x_new[0], x_new[1], x_new[2], x_new[3], f(x_new[0], x_new[1], x_new[2], x_new[3])))

        
        if sum((x_new[i] - x[i])**2 for i in range(4))**0.5 < tol:
            break
        x = x_new

    return x, history


initial_point = [2.0, 2.0, 4.0, 4.0]

optimal_values, history = projected_gradient_descent(initial_point)

highlighted_result = {
    "x1 (óptimo)": optimal_values[0],
    "x2 (óptimo)": optimal_values[1],
    "y1 (óptimo)": optimal_values[2],
    "y2 (óptimo)": optimal_values[3],
    "Valor mínimo de la función objetivo": f(optimal_values[0], optimal_values[1], optimal_values[2], optimal_values[3]),
}

highlighted_result
