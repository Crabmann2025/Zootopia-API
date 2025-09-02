import html
import data_fetcher  # Import the new module

# ------------------ Helper Functions ------------------

def get_name(animal):
    return animal.get("name")

def get_diet(animal):
    return animal.get("characteristics", {}).get("diet")

def get_type(animal):
    return animal.get("characteristics", {}).get("type")

def get_locations(animal):
    locs = animal.get("locations", [])
    return ", ".join(locs) if locs else None

# ------------------ HTML Serialization ------------------

def serialize_animal(animal):
    parts = ['<li class="cards__item">']

    name = get_name(animal)
    diet = get_diet(animal)
    locations = get_locations(animal)
    typ = get_type(animal)

    if name:
        parts.append(f'    <div class="card__title">{html.escape(name)}</div>')

    parts.append('    <div class="card__text">')
    parts.append('        <ul>')
    if diet:
        parts.append(f'            <li><strong>Diet:</strong> {html.escape(diet)}</li>')
    if locations:
        parts.append(f'            <li><strong>Location:</strong> {html.escape(locations)}</li>')
    if typ:
        parts.append(f'            <li><strong>Type:</strong> {html.escape(typ)}</li>')
    parts.append('        </ul>')
    parts.append('    </div>')

    parts.append('</li>')
    return "\n".join(parts)

def render_animals(data):
    return "\n".join(serialize_animal(a) for a in data)

# ------------------ Template Replacement ------------------

def replace_placeholder(template_file, placeholder, replacement):
    with open(template_file, "r", encoding="utf-8") as f:
        content = f.read()
    if placeholder not in content:
        raise ValueError(f"Placeholder '{placeholder}' not found in template.")
    return content.replace(placeholder, replacement, 1)

# ------------------ Main ------------------

def main():
    template_file = "animals_template.html"
    output_file = "animals.html"
    placeholder = "{{ANIMALS}}"

    # User input
    animal_name = input("Enter the name of an animal: ").strip()
    if not animal_name:
        print("No animal name entered. Aborting.")
        return

    # Fetch data via data_fetcher
    animals = data_fetcher.fetch_data(animal_name)

    if not animals:
        # Milestone 3: friendly error message on the website
        animals_html = f'''
        <div style="text-align:center; padding:50px; font-family:Arial, sans-serif;">
            <h2>The animal "{html.escape(animal_name)}" doesn't exist 😢</h2>
            <p>Try another name or check your spelling!</p>
        </div>
        '''
    else:
        animals_html = render_animals(animals)

    # Replace placeholder in template
    final_html = replace_placeholder(template_file, placeholder, animals_html)

    # Save output
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✔ {output_file} successfully generated!")

# ------------------ Script Start ------------------

if __name__ == "__main__":
    main()
