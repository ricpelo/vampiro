import parser as d

vestibulo = (
    'VESTÍBULO',
    'Estás en el vestíbulo del castillo...'
)

pasillo = (
    'PASILLO',
    'Te encuentras en medio del pasillo principal...'
)

cocina = (
    'COCINA',
    'Estás en la cocina del castillo...'
)

biblioteca = (
    'BIBLIOTECA',
    'Te hallas en la biblioteca del castillo...'
)

conexiones = {
    vestibulo: {d.NORTE: pasillo},
    pasillo: {d.SUR: vestibulo, d.ESTE: biblioteca, d.OESTE: cocina}
}

actual = None
