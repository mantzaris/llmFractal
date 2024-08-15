

function mandelbrot(c, max_iter)
    z = c
    for n in 1:max_iter
        if abs(z) > 2
            return n - 1
        end
        z = z^2 + c
    end
    return max_iter
end



