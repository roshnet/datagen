# datagen
## Generate random dataset in CSV format, and of required size.


### Usage
The basic usage syntax is:
> `python app.py SIZE`
where `SIZE` is an integer telling the number of records
to be contained in the dataset (defaults to 1000).

On entering this command right, the user is asked about
the dataset headers, or column names. The names of the headers are to be entered
on each prompt, and a empty repsonse starts a new prompt, in which the data-type of
each header is to be entered.

Here's a quick demo of how this might look.
> `python app.py 10`
> `Column 1 name: ` name
> `Column 2 name: ` temperature_C
> `Column 3 name: ` sweat_level
> `Column 4 name: ` hydration_level
> `Column 5 name: ` has_fever
> `Column 6 name:`

> `Type for "name"`: char 4 10
> `Type for "temperature"`: int 36 40
> `Type for "sweat_level"`: int 0 10
> `Type for "hydration_level"`: int 1 10
> `Type for "is_alcoholic"`: bool 0 1
