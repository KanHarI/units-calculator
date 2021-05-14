from units_calculator.all import parse


def test_biology_solutions_1() -> None:
    """Convert 5 ug/ul to mM and compare with a 20mM solution"""
    solution1_concentraion_by_mass = parse("5ug/ul")
    solution2_molar_concentration = parse("20mM")
    molecular_weight = parse("544.43g/mol")
    solution1_molar_concentration = solution1_concentraion_by_mass / molecular_weight
    sol2_to_sol1_concentraion_ratio = (
        solution2_molar_concentration / solution1_molar_concentration
    )
    if solution1_molar_concentration > solution2_molar_concentration:
        print("Solution 1 is stronger!")
    else:
        print("Solution 2 is stronger!")
    print(
        f"Solution 2 is {solution2_molar_concentration - solution1_molar_concentration} mM over solution 1"
    )
    print(
        f"Solution 2 [20mM] is {sol2_to_sol1_concentraion_ratio} as strong as solution 1 [5ug/ul]"
    )


def test_biology_solutions_2() -> None:
    """Dilute a given amount of source material to solution of the required size
    10mg to 120ug/ul"""
    original_mass = parse("10mg")
    target_conventration_by_mass = parse("120ug/ul")
    required_volume = original_mass / target_conventration_by_mass
    print(f"Required diluting agent volume is {required_volume}")


def test_biological_solutions_3() -> None:
    """5mg powder to 20mM"""
    powder_mass = parse("5mg")
    target_dilution = parse("20mM")
    powder_molecular_weight = parse("544.43g/mol")
    powder_mols = powder_mass / powder_molecular_weight
    diluting_agent_volume = powder_mols / target_dilution
    print(
        f"The required diluting agent volume is {diluting_agent_volume.conv_parsed_units('ul')}"
    )


# def dilution_series(concentrations_and_src_volumes: list[tuple[Unit, Unit]]) -> None:
