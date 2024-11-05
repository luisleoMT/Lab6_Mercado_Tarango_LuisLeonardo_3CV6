def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Calcula el área y actualiza el área máxima si es necesario
        current_area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, current_area)
        
        # Mueve los punteros
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

# Ejemplo de uso
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("El área máxima es:", max_area(height))
