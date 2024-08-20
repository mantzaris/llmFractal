using CSV
using DataFrames

function generate_simple_data(file_name)
    data = DataFrame(x = rand(100), y = rand(100))
    CSV.write(file_name, data)
    println("Julia: Data saved to $file_name")
end
