-- 1. List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT e.emp_no "Employee Number", e.last_name "Last Name", e.first_name "First Name", e.gender "Gender", s.salary "Salary" FROM employees e
INNER JOIN salaries s on e.emp_no = s.emp_no
ORDER BY e.emp_no;

-- 2. List employees who were hired in 1986.
SELECT e.emp_no "Employee Number", e.first_name "First Name", e.last_name "Last Name", e.hire_date "Hire Date" FROM employees e
WHERE e.hire_date BETWEEN '1986-01-01' and '1986-12-31'
ORDER BY e.hire_date;

-- 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT dm.dept_no "Department Number", d.dept_name "Department Name", dm.emp_no "Employee Number", e.last_name "Last Name", e.first_name "First Name", dm.from_date "Start Date", dm.to_date "End Date" FROM dept_manager dm
INNER JOIN departments d on dm.dept_no = d.dept_no
INNER JOIN employees e on dm.emp_no = e.emp_no;

-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT e.emp_no "Employee Number", e.last_name "Last Name", e.first_name "First Name", d.dept_name "Department Name" FROM employees e
INNER JOIN dept_emp de on e.emp_no = de.emp_no
INNER JOIN departments d on de.dept_no = d.dept_no;

-- 5. List all employees whose first name is "Hercules" and last names begin with "B."
SELECT e.emp_no "Employee Number", e.first_name "First Name", e.last_name "Last Name" FROM employees e
WHERE e.first_name = 'Hercules' AND e.last_name LIKE 'B%';

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT e.emp_no "Employee Number", e.last_name "Last Name", e.first_name "First Name", d.dept_name "Department Name", d.dept_no "Department Number" FROM employees e
INNER JOIN dept_emp de on e.emp_no = de.emp_no
INNER JOIN departments d on de.dept_no = d.dept_no
WHERE d.dept_no = 'd007';

-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT e.emp_no "Employee Number", e.last_name "Last Name", e.first_name "First Name", d.dept_name "Department Name" FROM employees e
INNER JOIN dept_emp de on e.emp_no = de.emp_no
INNER JOIN departments d on de.dept_no = d.dept_no
WHERE d.dept_no = 'd007' OR d.dept_no = 'd005';

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT e.last_name "Last Name", count(e.last_name) "Employees with Last Name" FROM employees e
GROUP BY e.last_name
ORDER BY count(e.last_name) DESC;



