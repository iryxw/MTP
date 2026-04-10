use axum::{
    routing::{get, post},
    Router,
    Json,
    extract::State,
};
use serde::{Deserialize, Serialize};
use std::net::SocketAddr;
use std::sync::{Arc, Mutex};

#[derive(Serialize, Clone)]
struct Expense {
    name: String,
    amount: f64,
}

#[derive(Clone)]
struct AppState {
    expenses: Arc<Mutex<Vec<Expense>>>,
}

#[derive(Deserialize)]
struct CreateExpense {
    name: String,
    amount: f64,
}

async fn get_expenses(State(state): State<AppState>) -> Json<Vec<Expense>> {
    let expenses = state.expenses.lock().unwrap();
    Json(expenses.clone())
}

async fn add_expense(
    State(state): State<AppState>,
    Json(payload): Json<CreateExpense>,
) -> Json<Expense> {
    let mut expenses = state.expenses.lock().unwrap();

    let expense = Expense {
        name: payload.name,
        amount: payload.amount,
    };

    expenses.push(expense.clone());

    Json(expense)
}

async fn get_total(State(state): State<AppState>) -> Json<f64> {
    let expenses = state.expenses.lock().unwrap();
    let total: f64 = expenses.iter().map(|e| e.amount).sum();

    Json(total)
}

#[tokio::main]
async fn main() {
    println!("Rust API запущен: http://0.0.0.0:8000");

    let state = AppState {
        expenses: Arc::new(Mutex::new(Vec::new())),
    };

    let app = Router::new()
        .route("/expenses", get(get_expenses).post(add_expense))
        .route("/expenses/total", get(get_total))
        .with_state(state);

    let addr = SocketAddr::from(([0, 0, 0, 0], 8000));

    axum::serve(
        tokio::net::TcpListener::bind(addr).await.unwrap(),
        app,
    )
    .await
    .unwrap();
}