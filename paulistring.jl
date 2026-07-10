# paulistring.jl
module PauliString

export generate_pauli, multiply_pauli

# Пример функции: возвращает строку Паули
function generate_pauli(n::Int)
    return "X" * "^" * string(n)
end

# Пример функции: симуляция умножения матриц Паули
function multiply_pauli(p1::String, p2::String)
    if p1 == "X" && p2 == "Y"
        return "iZ"
    elseif p1 == p2
        return "I"
    end
    return "Unknown"
end

end # module
