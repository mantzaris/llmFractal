# fractal_data.jl
using CSV
using DataFrames

function generate_fractal_data(file_name)
    println("Julia: Generating fractal data...")
    
    # Simulated fractal data (replace with real fractal data generation)
    data = DataFrame(x = rand(100), y = rand(100))
    
    # Save the data to a CSV file
    CSV.write(file_name, data)
    println("Julia: Fractal data saved to $file_name")
end
