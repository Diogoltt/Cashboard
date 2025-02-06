const chartColors = {
    teal: '#00BFA5',
    gray: '#455A64',
    lightGray: '#ECEFF1'
};

const commonOptions = {
    maintainAspectRatio: false,
    responsive: true,
    layout: {
        padding: {
            left: 15,
            right: 25,
            top: 15,
            bottom: 15
        }
    }
};

// Income Chart
const incomeCtx = document.getElementById('incomeChart').getContext('2d');
new Chart(incomeCtx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago'],
        datasets: [{
            data: [2500, 3000, 2500, 4000, 3250, 1850, 3400, 4121],
            backgroundColor: chartColors.teal,
            barPercentage: 0.6,
            borderRadius: 2
        }]
    },
    options: {
        ...commonOptions,
        plugins: { 
            legend: { display: false }
        },
        scales: {
            y: {
                beginAtZero: true,
                border: {
                    display: false
                },
                grid: {
                    color: chartColors.lightGray
                },
                ticks: {
                    padding: 10,
                    font: {
                        size: 11
                    }
                }
            },
            x: {
                grid: {
                    display: false
                },
                ticks: {
                    font: {
                        size: 11
                    }
                }
            }
        }
    }
});

// Payment Method Chart
const paymentCtx = document.getElementById('paymentChart').getContext('2d');
new Chart(paymentCtx, {
    type: 'doughnut',
    data: {
        labels: ['Débito', 'Dinheiro'],
        datasets: [{
            data: [55, 45],
            backgroundColor: [chartColors.gray, chartColors.teal]
        }]
    },
    options: {
        ...commonOptions,
        cutout: '70%',
        radius: '85%',
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    boxWidth: 8,
                    boxHeight: 8,
                    padding: 20,
                    font: {
                        size: 11
                    }
                }
            }
        }
    }
});

// Income Sources Chart
const incomeSourceCtx = document.getElementById('incomeSourceChart').getContext('2d');
new Chart(incomeSourceCtx, {
    type: 'bar',
    data: {
        labels: ['Produtos', 'Prestador', 'Serviços', 'Poupança'],
        datasets: [{
            data: [13854, 10908, 5625, 1865],
            backgroundColor: chartColors.teal,
            barPercentage: 0.75,
            borderRadius: 2
        }]
    },
    options: {
        ...commonOptions,
        indexAxis: 'y',
        plugins: { 
            legend: { display: false }
        },
        scales: {
            x: {
                beginAtZero: true,
                border: {
                    display: false
                },
                grid: {
                    color: chartColors.lightGray
                },
                ticks: {
                    padding: 10,
                    font: {
                        size: 11
                    },
                    callback: value => value.toLocaleString('pt-BR')
                }
            },
            y: {
                grid: {
                    display: false
                },
                ticks: {
                    font: {
                        size: 11
                    }
                }
            }
        }
    }
});

// Expenses Chart
const expensesCtx = document.getElementById('expensesChart').getContext('2d');
new Chart(expensesCtx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago'],
        datasets: [{
            data: [3024, 4395, 2970, 2907, 3024, 2265, 1553, 2763],
            backgroundColor: chartColors.gray,
            barPercentage: 0.6,
            borderRadius: 2
        }]
    },
    options: {
        ...commonOptions,
        plugins: { 
            legend: { display: false }
        },
        scales: {
            y: {
                beginAtZero: true,
                border: {
                    display: false
                },
                grid: {
                    color: chartColors.lightGray
                },
                ticks: {
                    padding: 10,
                    font: {
                        size: 11
                    }
                }
            },
            x: {
                grid: {
                    display: false
                },
                ticks: {
                    font: {
                        size: 11
                    }
                }
            }
        }
    }
});

// Income vs Expenses Chart
const incomeVsExpensesCtx = document.getElementById('incomeVsExpensesChart').getContext('2d');
new Chart(incomeVsExpensesCtx, {
    type: 'doughnut',
    data: {
        labels: ['Despesa', 'Receita'],
        datasets: [{
            data: [82, 18],
            backgroundColor: [chartColors.gray, chartColors.teal]
        }]
    },
    options: {
        ...commonOptions,
        cutout: '70%',
        radius: '85%',
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    boxWidth: 8,
                    boxHeight: 8,
                    padding: 20,
                    font: {
                        size: 11
                    }
                }
            }
        }
    }
});

// Expense Sources Chart
const expenseSourceCtx = document.getElementById('expenseSourceChart').getContext('2d');
new Chart(expenseSourceCtx, {
    type: 'bar',
    data: {
        labels: ['Marketing', 'Produtos', 'Consultoria', 'Seguro', 'Serviços', 'Promoções', 'Custos', 'Aluguel', 'Reformas'],
        datasets: [{
            data: [5267, 3127, 3002, 2895, 2401, 2024, 1952, 1596, 637],
            backgroundColor: chartColors.gray,
            barPercentage: 0.75,
            borderRadius: 2
        }]
    },
    options: {
        ...commonOptions,
        indexAxis: 'y',
        plugins: { 
            legend: { display: false }
        },
        scales: {
            x: {
                beginAtZero: true,
                border: {
                    display: false
                },
                grid: {
                    color: chartColors.lightGray
                },
                ticks: {
                    padding: 10,
                    font: {
                        size: 11
                    },
                    callback: value => value.toLocaleString('pt-BR')
                }
            },
            y: {
                grid: {
                    display: false
                },
                ticks: {
                    font: {
                        size: 11
                    }
                }
            }
        }
    }
});